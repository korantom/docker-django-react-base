#!/bin/bash
bash 

cd /app/frontend/frontend

echo "Installing packages..."
yarn install

echo "Starting server..."
yarn start
