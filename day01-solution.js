#!/usr/bin/env node

input = require('fs').readFileSync(0).toString().trim()

input = input.split('\n').map(line => parseInt(line, 10))

increased = 0
for (i = 0; i < input.length - 1; i++) {
	if (input[i+1] > input[i])
		increased++
}
console.log('part 1:', increased)

increased = 0
for (i = 0; i < input.length - 3; i++) {
	a = input[i] + input[i+1] + input[i+2]
	b = input[i+1] + input[i+2] + input[i+3]
	if (b > a)
		increased++
}
console.log('part 2:', increased)