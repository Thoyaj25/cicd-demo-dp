- name: Run tests
  run: |
    export PYTHONPATH="${PYTHONPATH}:."
    pytest
