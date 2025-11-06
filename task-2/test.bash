#!/bin/bash


echo "Running test"

sleep 3

docker compose logs client

if docker compose logs client | grep -q "Nobody expects the Spanish Inquisition!"; then
  echo "message found"
else
  echo "message not found"
fi

