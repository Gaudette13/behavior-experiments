import RPi.GPIO as GPIO
import time
import threading



GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)




class lickport():
    
    def __init(self, lickport_pin, side):
        
        self.lickport_pin = lickport_pin
        self.side = side
        

    def Lick(self, sampling_rate, sampling_duration):
        
        GPIO.setup(self.lickport_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        #records the licks at a given sampling rate
    #    _licks = []
    #    _t_licks = []
    
        #calculate the number of samples needed
        num_samples = int(sampling_duration * sampling_rate)
    
        for i in range(num_samples):
    
            if GPIO.input(self.lickport_pin):
    #            #register lick
    #            _licks.append(1)
    #            _t_licks.append(time.time())
                print(f'{self.side} lick')
    
            else:
    #            #register no lick
    #            _licks.append(0)
    #            _t_licks.append(time.time())
                print('No lick')
    
            #wait for next sample and update step
            time.sleep(1/sampling_rate)
            
left = lickport(12, 'left')
right = lickport(16, 'right')

thread_L = threading.Thread(target = left.Lick, args = (20, 30))
thread_R = threading.Thread(target = right.Lick, args = (20, 30))

thread_L.start()
thread_R.start()