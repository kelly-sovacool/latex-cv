#!/bin/bash
sed -e 's/month = \([a-z]*\),/month = {\1},/' $1 > $2