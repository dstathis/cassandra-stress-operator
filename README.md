# cassandra-stress-operator

## Description

A charm of cassandra-stress. This charm can be used to stress test a cassandra cluster. It also has a simple test used just for testing that the cassandra charm is functioning correctly.

## Usage

    juju run-action cassandra-stress/[unit-id] simpletest

## Developing

Create and activate a virtualenv with the development requirements:

    virtualenv -p python3 venv
    source venv/bin/activate
    pip install -r requirements-dev.txt

## Testing

The Python operator framework includes a very nice harness for testing
operator behaviour without full deployment. Just `run_tests`:

    ./run_tests
