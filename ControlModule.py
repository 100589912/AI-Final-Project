# Import required dependencies
import numpy as np
import mdptoolbox

class ControlModule:
    def __init__(self):
        """ Dummy constructor to use the Python Class as a namespace """
        pass

    @staticmethod
    def generate_P(prob_tables,n_states) -> np.ndarray:
        """ Function that generates the probabilities (transition) matrix """
        ### TO BE COMPLETED BY THE STUDENTS ###
        ...
        P = np.zeros((3, n_states, n_states))
        deltas = {
            "decrease": [-2, -1, 0],
            "maintain": [-1, 0, +1],
            "increase": [0, +1, +2]
        }
        for a_idx, action in enumerate(["decrease", "maintain", "increase"]):
            table = prob_tables[action]        
            action_dts = deltas[action]
            for s in range(n_states):
                for delta, p in zip(action_dts, table):
                    next_s = s + delta
                    if next_s < 0:
                        next_s = 0
                    elif next_s >= n_states:
                        next_s = n_states - 1
                    P[a_idx, s, next_s] += p
        return P

    @staticmethod
    def generate_R(demand,n_states) -> np.ndarray:
        """ Function that generates the rewards (costs) matrix """
        ### TO BE COMPLETED BY THE STUDENTS ###
        ...
        R = np.zeros((3, n_states))
        for s in range(n_states):
            level = s / 100.0           
            base_cost = abs(demand - level)
            for a in range(3):

                if a == 0:        # decrease
                    direction = -1
                elif a == 1:      # maintain
                    direction = 0
                else:             # increase
                    direction = +1
                # penalty 
                if direction > 0 and demand < level:
                    cost = base_cost * 2
                elif direction < 0 and demand > level:
                    cost = base_cost * 2
                else:
                    cost = base_cost
                R[a, s] = -cost
        return R

    @staticmethod
    def control_iteration() -> np.int32:
        """ Function that computes one control-iteration """
        ### TO BE COMPLETED BY THE STUDENTS ###
        ...

    @staticmethod
    def control_loop(demand: np.ndarray, 
                     probs: np.ndarray,
                     n_states: np.int32, 
                     n_actions: np.int32,
                     gamma: np.float64) -> np.ndarray:
        """ Function that computes all the required iterations (control-loop) to satisfy the power demand """
        ### TO BE COMPLETED BY THE STUDENTS ###

        ### DUMMY BEHAVIOUR TO PREVENT CRASHING (MUST BE DELETED AFTER THE FULL IMPLEMENTATION) ###
        return np.zeros_like(a=demand, dtype=np.float64)
        ### ###
