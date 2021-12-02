#!/usr/bin/env awk -f

{
	if ($1 > prev) {
		increased++
	}
	prev=$1
}

END { print increased-1 }
