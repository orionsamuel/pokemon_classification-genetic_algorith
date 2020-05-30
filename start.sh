#!/bin/sh

if grep -q "$USR" /etc/passwd
then
  adduser --system --no-create-home --disabled-password --quiet --group "$USR"
else
  echo "Not Possible"
fi
python main.py
chown "$USR":"$USR" *.csv
rm -r __pycache__
exit 0
