function collatzSteps(n) {
    let steps = 0;

    while (n !== 1) {
        if (n % 2 === 0) {
            n = Math.floor(n / 2);
        } else {
            n = 3 * n + 1;
        }

        steps++;
    }

    return steps;
}

const LIMIT = 100000;

const start = performance.now();

let totalSteps = 0;

for (let i = 1; i <= LIMIT; i++) {
    totalSteps += collatzSteps(i);
}

const end = performance.now();

console.log(`Tiempo: ${(end - start).toFixed(2)} ms`);
console.log(`Pasos totales: ${totalSteps}`);