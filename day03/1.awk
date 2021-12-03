#!/usr/bin/env -S awk -f

BEGIN { FS="" }

{
    for (i=1; i<=NF; i++) {
        c[i]+=$i
    }
}

END {
    epsilon=0
    for (i=1; i<=NF; i++) {
        gamma+=(c[i] > NR/2) * 2^(NF-i)
        epsilon+=(c[i] < NR/2) * 2^(NF-i)
    }
    print gamma " " epsilon
    print gamma * epsilon
}
