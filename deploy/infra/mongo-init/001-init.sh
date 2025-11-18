#!/bin/bash
set -e

# Wait for MongoDB to be ready
until mongosh --host localhost -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin --eval "db.adminCommand('ping')" &>/dev/null; do
  echo "Waiting for MongoDB to be ready..."
  sleep 2
done

echo "MongoDB is ready. Creating application user..."

# Switch to application database and create user with read/write permissions
mongosh -u "$MONGO_INITDB_ROOT_USERNAME" -p "$MONGO_INITDB_ROOT_PASSWORD" --authenticationDatabase admin <<EOF
use opty;

db.createUser({
  user: "$MONGO_APP_USER",
  pwd: "$MONGO_APP_PASSWORD",
  roles: [
    { role: "readWrite", db: "opty" }
  ]
});

print("Application user created successfully!");
EOF

echo "MongoDB initialization completed."
