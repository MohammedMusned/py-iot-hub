# back-end-tech-interview APIs

This is an overview of the main API endpoints in this project


## Authentication
- **POST** `/api/login` - Authenticate an existing user and return a JWT token.

## Users
- **POST** `/api/users` - Register a new user.
- **GET** `/api/users` - Retrieve a list of all users.
- **GET** `/api/users/me` - Retrieve information about the currently logged-in user.

## Devices
- **GET** `/api/devices` - Retrieve a list of all IoT devices.
- **POST** `/api/devices` - Register a new IoT device.

## Telemetry
- **GET** `/api/telemetry` - Retrieve telemetry data. Accepts an optional `device_id` query parameter to filter by a specific device.
