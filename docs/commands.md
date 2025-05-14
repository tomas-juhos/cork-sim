# Useful commands

## Console

### Spin-up
```commandline
docker-compose up -d dev
```

### Step-in
```commandline
docker-compose exec dev bash
```

### Tear-down
```commandline
docker-compose down
```

## Ape Environment

### Step-in local ape console
```commandline
ape console --network ethereum:local:foundry
```

### Run script
```commandline
ape run <script> --network ethereum:local:foundry
```