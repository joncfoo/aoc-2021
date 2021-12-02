#!/usr/bin/env awk -f

{
	if (b+c+d > a+b+c) {
		increased++
	}
	a=b; b=c; c=d; d=$1;
}

END { print increased-2 }
