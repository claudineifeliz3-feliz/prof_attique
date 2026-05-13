

const { performance } = require("perf_hooks");

// ── Funções ──────────────────────────────────────────────
function somaRecursiva(lista) {
    if (lista.length === 0) return 0;
    return lista[0] + somaRecursiva(lista.slice(1));
}

function somaFor(lista) {
    let total = 0;
    for (let n of lista) total += n;
    return total;
}

function somaWhile(lista) {
    let total = 0;
    let i = 0;
    while (i < lista.length) {
        total += lista[i];
        i++;
    }
    return total;
}

function somaReduce(lista) {
    return lista.reduce((acc, n) => acc + n, 0);
}

// ── Benchmark ────────────────────────────────────────────
function benchmark(nome, fn, lista, N) {
    const inicio = performance.now();
    for (let i = 0; i < N; i++) fn(lista);
    const fim = performance.now();
    return { nome, tempo: (fim - inicio) / 1000 };
}

const numeros = [3, 8, 20, 21, 34, 44];
const N = 100_000;

const resultados = [
    benchmark("Recursiva",  somaRecursiva, numeros, N),
    benchmark("Loop for",   somaFor,       numeros, N),
    benchmark("Loop while", somaWhile,     numeros, N),
    benchmark("reduce()",   somaReduce,    numeros, N),
];

// Ordena do mais lento ao mais rápido
resultados.sort((a, b) => b.tempo - a.tempo);

const maiRapido = Math.min(...resultados.map(r => r.tempo));

// ── Exibição ─────────────────────────────────────────────
console.log(`${"Método".padEnd(12)} ${"Tempo (s)".padStart(10)} ${"Comparação".padStart(15)}`);
console.log("-".repeat(40));

for (const { nome, tempo } of resultados) {
    const comparacao = (tempo / maiRapido).toFixed(1) + "x";
    console.log(`${nome.padEnd(12)} ${tempo.toFixed(4).padStart(9)}s ${comparacao.padStart(15)}`);
}