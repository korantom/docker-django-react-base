#!/bin/bash
bash 

cd /app/frontend

echo "Creating React App ..."
yarn create react-app frontend

cd frontend
# chown node:node -R .

echo "Installing packages..."
yarn install

echo "Starting server..."
yarn start
