#!/bin/bash
sed -e 's/month = \([a-zA-Z]*\),/month = {\1},/' $1 > $2
