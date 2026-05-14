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
    def control_iteration(P: np.ndarray,
                          R: np.ndarray,
                          state: np.int32,
                          gamma: np.float64)-> np.int32:
    
        """ Function that computes one control-iteration """
        ### TO BE COMPLETED BY THE STUDENTS ###
    solver = mdtoolbox.mdp.ValueIteration(P,R,gamma)
    solver.run()
    policy = np.array(solver.policy) 
    return np.int32(policy[state]) 

    @staticmethod
    def control_loop(demand: np.ndarray, 
                     probs: np.ndarray,
                     n_states: np.int32, 
                     n_actions: np.int32,
                     gamma: np.float64) -> np.ndarray:
        """ Function that computes all the required iterations (control-loop) to satisfy the power demand """
        ### TO BE COMPLETED BY THE STUDENTS ###
        prob_tables = {
            "decrease": probs[0], 
            "maintain": probs[1], 
            "increase": probs[2]
        }
        P = ControlModule.generate_P(prob_tables = prob_tables, n_states=n_states) 
        response = np.zeros_like(a=demand, dtype=np.float64) 
        current_state = np.int32(round(demand[0] * (n_states - 1))) 
        movements = {
            0:[-2,-1,0],
            1:[-1,0,+1],
            2:[0,+1,+2]
        } 
        for t in range(demand.shape[0]):
        R = ControlModule.generate_R(demand=demand[t], n_states=n_states) 
        action = ControlModule.control_iteration( 
            P=P, 
            R=R,
            state=current_state, 
            gamma=gamma
        )
        selected_movement = np.random.choice(
            movements[int(action)],
            p=probs[int(action)]
        ) 
        next_state = current_state + selected_movement
        next_state= max(0, min(n_states -1, next_state))
        current_state = np.int32(next_state) 
        response[t] = current_state / 100.0
return response 
                    
                         
                         
                         
                         
        
