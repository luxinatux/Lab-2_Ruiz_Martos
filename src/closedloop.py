"""
    @file           TP_closedloop.py
    @brief          Driver class implementing a closed loop controller.
    @details        Implements a closed loop P-Only controller for any system.
"""

class TP_ClosedLoop:
    ''' @brief      Closed loop feedback control class              
        @details    Objects of this class can be used to apply closed
                    closed loop feedback control to the velocity of the
                    motors
    '''
    def __init__(self, Gain_Vector):
        ''' @brief                  Initializes and returns a Closed_Loop object          
            @details                The controller driver implements a P_only closed loop 
                                    controller and creates mutable gain values.
            @param Gain_Vector      The proportional gains of the closed-loop controller. 
                        
        '''
        ## Proportional gain value
        self.Gain_Vector = Gain_Vector
    
        
    def update(self, Reference_Vector, Measured_Vector):
        ''' @brief                      Updates the error value of the proportional controller
            @details                    Updates and calculates the error value of the 
                                        proportional controller based on the inputs of the 
                                        measured and reference values.
            @param Reference_Vector     Reference input values based on desired values.
            @param Measured_Vector      Inputs of measured data from the system, which is used to calculate the error.
        
        '''
        self.actuation = 0
        self.max_lim = 100
        self.min_lim = -100
        self.r = 2.21
        self.k_t = 13.8
        self.V_DC = 12
        self.Reference_Vector =  Reference_Vector 
        self.Measured_Vector =  Measured_Vector 
        
        
        for self.idx in range(4):
            self.actuation += self.Gain_Vector[self.idx]*(self.Reference_Vector[self.idx]-self.Measured_Vector[self.idx])
#            self.actuation_2 =  self.a + self.actuation
#            self.a = self.actuation
        
        self.duty = ((100*self.r)/(4*self.k_t*self.V_DC))*self.actuation
        
        
        if self.duty >= self.max_lim:
            self.duty = self.max_lim
        elif self.duty <= self.min_lim:
            self.duty = self.min_lim 
        
        return self.duty
   
    def get_Kp(self):
        ''' @brief      Returns the proportional gain     
            @return     Returns the proportional gain set using the 
                        set_Kp function
        '''
        
        return self.Gain_Vector
    
    def set_K_Vector(self,Gain_Vector):
        ''' @brief               Sets the value of the proportional gain
            @param Gain_Vector   The proportional gains of the closed-loop controller.
        '''
        
        self.Gain_Vector = Gain_Vector
        
    
        