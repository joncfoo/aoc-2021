#!/usr/bin/env awk -f

/^forward / {x+=$2}
/^up / {v-=$2}
/^down / {v+=$2}

END { print x * v }
