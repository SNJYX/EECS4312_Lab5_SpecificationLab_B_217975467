## Student Name: Sanjay Raveendran
## Student ID: 217975467

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
   
    usage = {resource: 0 for resource in resources}

    for request in requests:
        if not isinstance(request, dict):
            raise ValueError("Each request must be a dictionary")

        for resource, amount in request.items():
            if resource not in resources:
                return False

            usage[resource] += amount

            if usage[resource] > resources[resource]:
                return False

    # NEW REQUIREMENT:
    # At least one resource must remain unallocated
    all_fully_consumed = all(
        usage[resource] == resources[resource]
        for resource in resources
    )

    if all_fully_consumed:
        return False

    return True
