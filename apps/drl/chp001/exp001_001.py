#

class Exp001001(object):
    def __init__(self):
        self.refl = ''

    def startup(self):
        #self.bandit_walk()
        #self.bandit_slippery_walk()
        #self.random_walk()
        #self.gridworld()
        self.frozen_lake()

    def bandit_walk(self):
        P = {
            0: {
                0: [(1.0, 0, 0.0, True)],
                1: [(1.0, 0, 0.0, True)]
            },
            1: {
                0: [(1.0, 0, 0.0, True)],
                1: [(1.0, 2, 1.0, True)]
            },
            2: {
                0: [(1.0, 2, 0.0, True)],
                1: [(1.0, 2, 0.0, True)]
            }
        }
        print(P)

    def bandit_slippery_walk(self):
        P = {
            0: {
                0: [(1.0, 0, 0.0, True)],
                1: [(1.0, 0, 0.0, True)]
            },
            1: {
                0: [(0.8, 0, 0.0, True), (0.2, 2, 1.0, True)],
                1: [(0.8, 2, 1.0, True), (0.2, 0, 0.0, True)]
            },
            2: {
                0: [(1.0, 2, 0.0, True)],
                1: [(1.0, 2, 0.0, True)]
            }
        }
        print(P)

    def random_walk(self):
        P = {
            0: {
                0: [(1.0, 0, 0.0, True)],
                1: [(1.0, 0, 0.0, True)]
            },
            1: {
                0: [(0.5, 0, 0.0, True), (0.5, 2, 0.0, False)],
                1: [(0.5, 2, 0.0, False), (0.5, 0, 0.0, True)]
            },
            2: {
                0: [(0.5, 1, 0.0, False), (0.5, 3, 0.0, False)],
                1: [(0.5, 3, 0.0, False), (0.5, 1, 0.0, False)]
            },
            3: {
                0: [(0.5, 2, 0.0, False), (0.5, 4, 0.0, False)],
                1: [(0.5, 4, 0.0, False), (0.5, 2, 0.0, False)]
            },
            4: {
                0: [(0.5, 3, 0.0, False), (0.5, 5, 0.0, False)],
                1: [(0.5, 5, 0.0, False), (0.5, 3, 0.0, False)]
            },
            5: {
                0: [(0.5, 4, 0.0, False), (0.5, 6, 1.0, True)],
                1: [(0.5, 6, 1.0, True), (0.5, 4, 0.0, False)]
            },
            6: {
                0: [(1.0, 6, 0.0, True)],
                1: [(1.0, 6, 0.0, True)]
            }
        }
        print('Random Walk: {0};'.format(P))

    def gridworld(self):
        # Russell and Norvig's Gridworld: 
        # stochastic environment (80% action success, 20.00% split evenly in right angles)
        # 3x4 grid, 12 states 0-11
        # -0.04 time step penalty, 
        # +1 for landing in state 3 (top right corner), 
        # -1 for landing in state 7 (below state 3)
        # state 5 is a wall, agents attempting to get in that cell will bounce back
        # episodic environment, the agent terminates when it lands in state 3 or 7
        # agent starts in state 0 (top left corner)
        # actions left (0), down (1), right (2), up (3)
        P = {
            0: {
                0: [(0.9, 0, -0.04, False),
                    (0.1, 4, -0.04, False)
                ],
                1: [(0.1, 0, -0.04, False), (0.8, 4, -0.04, False), (0.1, 1, -0.04, False)],
                2: [(0.1, 4, -0.04, False), (0.8, 1, -0.04, False), (0.1, 0, -0.04, False)],
                3: [(0.1, 1, -0.04, False), (0.8, 0, -0.04, False), (0.1, 0, -0.04, False)]
            },
            1: {
                0: [(0.2, 1, -0.04, False),
                    (0.8, 0, -0.04, False)
                ],
                1: [(0.1, 0, -0.04, False), (0.8, 1, -0.04, False), (0.1, 2, -0.04, False)],
                2: [(0.1, 1, -0.04, False), (0.8, 2, -0.04, False), (0.1, 1, -0.04, False)],
                3: [(0.1, 2, -0.04, False), (0.8, 1, -0.04, False), (0.1, 0, -0.04, False)]
            },
            2: {
                0: [(0.1, 2, -0.04, False),
                    (0.8, 1, -0.04, False),
                    (0.1, 6, -0.04, False)
                ],
                1: [(0.1, 1, -0.04, False), (0.8, 6, -0.04, False), (0.1, 3, 0.96, True)],
                2: [(0.1, 6, -0.04, False), (0.8, 3, 0.96, True), (0.1, 2, -0.04, False)],
                3: [(0.1, 3, 0.96, True), (0.8, 2, -0.04, False), (0.1, 1, -0.04, False)]
            },
            3: {
                0: [(1.0, 3, 0, True)],
                1: [(1.0, 3, 0, True)],
                2: [(1.0, 3, 0, True)],
                3: [(1.0, 3, 0, True)]
            },
            4: {
                0: [(0.1, 0, -0.04, False),
                    (0.8, 4, -0.04, False),
                    (0.1, 8, -0.04, False)
                ],
                1: [(0.2, 4, -0.04, False), (0.8, 8, -0.04, False)],
                2: [(0.1, 8, -0.04, False), (0.8, 4, -0.04, False), (0.1, 0, -0.04, False)],
                3: [(0.2, 4, -0.04, False), (0.8, 0, -0.04, False)]
            },
            5: {
                0: [(1.0, 5, 0, True)],
                1: [(1.0, 5, 0, True)],
                2: [(1.0, 5, 0, True)],
                3: [(1.0, 5, 0, True)]
            },
            6: {
                0: [(0.1, 2, -0.04, False),
                    (0.8, 6, -0.04, False),
                    (0.1, 10, -0.04, False)
                ],
                1: [(0.1, 6, -0.04, False), (0.8, 10, -0.04, False), (0.1, 7, -1.04, True)],
                2: [(0.1, 10, -0.04, False), (0.8, 7, -1.04, True), (0.1, 2, -0.04, False)],
                3: [(0.1, 7, -1.04, True), (0.8, 2, -0.04, False), (0.1, 6, -0.04, False)]
            },
            7: {
                0: [(1.0, 7, 0, True)],
                1: [(1.0, 7, 0, True)],
                2: [(1.0, 7, 0, True)],
                3: [(1.0, 7, 0, True)]
            },
            8: {
                0: [(0.1, 4, -0.04, False),
                    (0.9, 8, -0.04, False)
                ],
                1: [(0.9, 8, -0.04, False), (0.1, 9, -0.04, False)],
                2: [(0.1, 8, -0.04, False), (0.8, 9, -0.04, False), (0.1, 4, -0.04, False)],
                3: [(0.1, 9, -0.04, False), (0.8, 4, -0.04, False), (0.1, 8, -0.04, False)]
            },
            9: {
                0: [(0.2, 9, -0.04, False),
                    (0.8, 8, -0.04, False)
                ],
                1: [(0.1, 8, -0.04, False), (0.8, 9, -0.04, False), (0.1, 10, -0.04, False)],
                2: [(0.2, 9, -0.04, False), (0.8, 10, -0.04, False)],
                3: [(0.1, 10, -0.04, False),
                    (0.8, 9, -0.04, False),
                    (0.1, 8, -0.04, False)
                ]
            },
            10: {
                0: [(0.1, 6, -0.04, False),
                    (0.8, 9, -0.04, False),
                    (0.1, 10, -0.04, False)
                ],
                1: [(0.1, 9, -0.04, False),
                    (0.8, 10, -0.04, False),
                    (0.1, 11, -0.04, False)
                ],
                2: [(0.1, 10, -0.04, False),
                    (0.8, 11, -0.04, False),
                    (0.1, 6, -0.04, False)
                ],
                3: [(0.1, 11, -0.04, False),
                    (0.8, 6, -0.04, False),
                    (0.1, 9, -0.04, False)
                ]
            },
            11: {
                0: [(0.1, 7, -1.04, True),
                    (0.8, 10, -0.04, False),
                    (0.1, 11, -0.04, False)
                ],
                1: [(0.1, 10, -0.04, False),
                    (0.9, 11, -0.04, False)
                ],
                2: [(0.9, 11, -0.04, False), (0.1, 7, -1.04, True)],
                3: [(0.1, 11, -0.04, False),
                    (0.8, 7, -1.04, True),
                    (0.1, 10, -0.04, False)
                ]
            }
        }
        print('Gridworld: {0};'.format(P))

    def frozen_lake(self):
        # Frozen Lake Gridworld: 
        # highly stochastic environment (33.33% action success, 66.66% split evenly in right angles)
        # 4x4 grid, 16 states 0-15
        # +1 for landing in state 15 (top bottom corner) 0 otherwise
        # states 5, 7, 11, and 12 are holes, agents die in holes, no penalty, just end of episode
        # state 15 is the goal, reaching it ends the episode too
        # agent starts in state 0 (top left corner)
        # actions left (0), down (1), right (2), up (3)
        P = {
            0: {
                0: [(0.6666666666666666, 0, 0.0, False),
                    (0.3333333333333333, 4, 0.0, False)
                ],
                1: [(0.3333333333333333, 0, 0.0, False),
                    (0.3333333333333333, 4, 0.0, False),
                    (0.3333333333333333, 1, 0.0, False)
                ],
                2: [(0.3333333333333333, 4, 0.0, False),
                    (0.3333333333333333, 1, 0.0, False),
                    (0.3333333333333333, 0, 0.0, False)
                ],
                3: [(0.3333333333333333, 1, 0.0, False),
                    (0.6666666666666666, 0, 0.0, False)
                ]
            },
            1: {
                0: [(0.3333333333333333, 1, 0.0, False),
                    (0.3333333333333333, 0, 0.0, False),
                    (0.3333333333333333, 5, 0.0, True)
                ],
                1: [(0.3333333333333333, 0, 0.0, False),
                    (0.3333333333333333, 5, 0.0, True),
                    (0.3333333333333333, 2, 0.0, False)
                ],
                2: [(0.3333333333333333, 5, 0.0, True),
                    (0.3333333333333333, 2, 0.0, False),
                    (0.3333333333333333, 1, 0.0, False)
                ],
                3: [(0.3333333333333333, 2, 0.0, False),
                    (0.3333333333333333, 1, 0.0, False),
                    (0.3333333333333333, 0, 0.0, False)
                ]
            },
            2: {
                0: [(0.3333333333333333, 2, 0.0, False),
                    (0.3333333333333333, 1, 0.0, False),
                    (0.3333333333333333, 6, 0.0, False)
                ],
                1: [(0.3333333333333333, 1, 0.0, False),
                    (0.3333333333333333, 6, 0.0, False),
                    (0.3333333333333333, 3, 0.0, False)
                ],
                2: [(0.3333333333333333, 6, 0.0, False),
                    (0.3333333333333333, 3, 0.0, False),
                    (0.3333333333333333, 2, 0.0, False)
                ],
                3: [(0.3333333333333333, 3, 0.0, False),
                    (0.3333333333333333, 2, 0.0, False),
                    (0.3333333333333333, 1, 0.0, False)
                ]
            },
            3: {
                0: [(0.3333333333333333, 3, 0.0, False),
                    (0.3333333333333333, 2, 0.0, False),
                    (0.3333333333333333, 7, 0.0, True)
                ],
                1: [(0.3333333333333333, 2, 0.0, False),
                    (0.3333333333333333, 7, 0.0, True),
                    (0.3333333333333333, 3, 0.0, False)
                ],
                2: [(0.3333333333333333, 7, 0.0, True),
                    (0.6666666666666666, 3, 0.0, False)
                ],
                3: [(0.6666666666666666, 3, 0.0, False),
                    (0.3333333333333333, 2, 0.0, False)
                ]
            },
            4: {
                0: [(0.3333333333333333, 0, 0.0, False),
                    (0.3333333333333333, 4, 0.0, False),
                    (0.3333333333333333, 8, 0.0, False)
                ],
                1: [(0.3333333333333333, 4, 0.0, False),
                    (0.3333333333333333, 8, 0.0, False),
                    (0.3333333333333333, 5, 0.0, True)
                ],
                2: [(0.3333333333333333, 8, 0.0, False),
                    (0.3333333333333333, 5, 0.0, True),
                    (0.3333333333333333, 0, 0.0, False)
                ],
                3: [(0.3333333333333333, 5, 0.0, True),
                    (0.3333333333333333, 0, 0.0, False),
                    (0.3333333333333333, 4, 0.0, False)
                ]
            },
            5: {
                0: [(1.0, 5, 0, True)],
                1: [(1.0, 5, 0, True)],
                2: [(1.0, 5, 0, True)],
                3: [(1.0, 5, 0, True)]
            },
            6: {
                0: [(0.3333333333333333, 2, 0.0, False),
                    (0.3333333333333333, 5, 0.0, True),
                    (0.3333333333333333, 10, 0.0, False)
                ],
                1: [(0.3333333333333333, 5, 0.0, True),
                    (0.3333333333333333, 10, 0.0, False),
                    (0.3333333333333333, 7, 0.0, True)
                ],
                2: [(0.3333333333333333, 10, 0.0, False),
                    (0.3333333333333333, 7, 0.0, True),
                    (0.3333333333333333, 2, 0.0, False)
                ],
                3: [(0.3333333333333333, 7, 0.0, True),
                    (0.3333333333333333, 2, 0.0, False),
                    (0.3333333333333333, 5, 0.0, True)
                ]
            },
            7: {
                0: [(1.0, 7, 0, True)],
                1: [(1.0, 7, 0, True)],
                2: [(1.0, 7, 0, True)],
                3: [(1.0, 7, 0, True)]
            },
            8: {
                0: [(0.3333333333333333, 4, 0.0, False),
                    (0.3333333333333333, 8, 0.0, False),
                    (0.3333333333333333, 12, 0.0, True)
                ],
                1: [(0.3333333333333333, 8, 0.0, False),
                    (0.3333333333333333, 12, 0.0, True),
                    (0.3333333333333333, 9, 0.0, False)
                ],
                2: [(0.3333333333333333, 12, 0.0, True),
                    (0.3333333333333333, 9, 0.0, False),
                    (0.3333333333333333, 4, 0.0, False)
                ],
                3: [(0.3333333333333333, 9, 0.0, False),
                    (0.3333333333333333, 4, 0.0, False),
                    (0.3333333333333333, 8, 0.0, False)
                ]
            },
            9: {
                0: [(0.3333333333333333, 5, 0.0, True),
                    (0.3333333333333333, 8, 0.0, False),
                    (0.3333333333333333, 13, 0.0, False)
                ],
                1: [(0.3333333333333333, 8, 0.0, False),
                    (0.3333333333333333, 13, 0.0, False),
                    (0.3333333333333333, 10, 0.0, False)
                ],
                2: [(0.3333333333333333, 13, 0.0, False),
                    (0.3333333333333333, 10, 0.0, False),
                    (0.3333333333333333, 5, 0.0, True)
                ],
                3: [(0.3333333333333333, 10, 0.0, False),
                    (0.3333333333333333, 5, 0.0, True),
                    (0.3333333333333333, 8, 0.0, False)
                ]
            },
            10: {
                0: [(0.3333333333333333, 6, 0.0, False),
                    (0.3333333333333333, 9, 0.0, False),
                    (0.3333333333333333, 14, 0.0, False)
                ],
                1: [(0.3333333333333333, 9, 0.0, False),
                    (0.3333333333333333, 14, 0.0, False),
                    (0.3333333333333333, 11, 0.0, True)
                ],
                2: [(0.3333333333333333, 14, 0.0, False),
                    (0.3333333333333333, 11, 0.0, True),
                    (0.3333333333333333, 6, 0.0, False)
                ],
                3: [(0.3333333333333333, 11, 0.0, True),
                    (0.3333333333333333, 6, 0.0, False),
                    (0.3333333333333333, 9, 0.0, False)
                ]
            },
            11: {
                0: [(1.0, 11, 0, True)],
                1: [(1.0, 11, 0, True)],
                2: [(1.0, 11, 0, True)],
                3: [(1.0, 11, 0, True)]
            },
            12: {
                0: [(1.0, 12, 0, True)],
                1: [(1.0, 12, 0, True)],
                2: [(1.0, 12, 0, True)],
                3: [(1.0, 12, 0, True)]
            },
            13: {
                0: [(0.3333333333333333, 9, 0.0, False),
                    (0.3333333333333333, 12, 0.0, True),
                    (0.3333333333333333, 13, 0.0, False)
                ],
                1: [(0.3333333333333333, 12, 0.0, True),
                    (0.3333333333333333, 13, 0.0, False),
                    (0.3333333333333333, 14, 0.0, False)
                ],
                2: [(0.3333333333333333, 13, 0.0, False),
                    (0.3333333333333333, 14, 0.0, False),
                    (0.3333333333333333, 9, 0.0, False)
                ],
                3: [(0.3333333333333333, 14, 0.0, False),
                    (0.3333333333333333, 9, 0.0, False),
                    (0.3333333333333333, 12, 0.0, True)
                ]
            },
            14: {
                0: [(0.3333333333333333, 10, 0.0, False),
                    (0.3333333333333333, 13, 0.0, False),
                    (0.3333333333333333, 14, 0.0, False)
                ],
                1: [(0.3333333333333333, 13, 0.0, False),
                    (0.3333333333333333, 14, 0.0, False),
                    (0.3333333333333333, 15, 1.0, True)
                ],
                2: [(0.3333333333333333, 14, 0.0, False),
                    (0.3333333333333333, 15, 1.0, True),
                    (0.3333333333333333, 10, 0.0, False)
                ],
                3: [(0.3333333333333333, 15, 1.0, True),
                    (0.3333333333333333, 10, 0.0, False),
                    (0.3333333333333333, 13, 0.0, False)
                ]
            },
            15: {
                0: [(1.0, 15, 0, True)],
                1: [(1.0, 15, 0, True)],
                2: [(1.0, 15, 0, True)],
                3: [(1.0, 15, 0, True)]
            }
        }
        print('Frozen Lake: {0};'.format(P))