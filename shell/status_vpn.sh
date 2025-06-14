#!/bin/bash

# Симуляция: случайно выдаёт "включено" или "выключено"
if [ -f vpn_running.txt ]; then
  echo "active (running)"
else
  echo "inactive (dead)"
fi
