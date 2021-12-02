#!/usr/bin/env awk -f

/^forward / {x+=$2; v+=a*$2}
/^up / {a-=$2}
/^down / {a+=$2}

END { print x * v }
