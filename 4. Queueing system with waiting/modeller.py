import numpy.random as nr


class UniformGenerator:
    def __init__(self, a, b):
        if not 0 <= a <= b:
            raise ValueError('Параметры должны удовлетворять условию 0 <= a <= b')
        self._a = a
        self._b = b

    def generate(self):
        return nr.uniform(self._a, self._b)


class NormalGenerator:
    def __init__(self, m, d):
        self._m = m
        self._d = d
    def generate    (self):
        return nr.normal(self._m, self._d)



class Model():
    def __init__(self, dt, req_count, reenter_prob):
        self.dt = dt
        self.req_count = req_count
        self.reenter_prob = reenter_prob

        self.queue = 0
        self.queue_len_max = 0
        self.reenter = 0
        
    def check_len_max(self):
        if self.queue > self.queue_len_max:
            self.queue_len_max = self.queue
        

    def add_to_queue(self):
        self.queue += 1
        self.check_len_max()


    def rem_from_queue(self, isReenter = True):
        if self.queue == 0:
            return 0

        self.queue -= 1
            
        if isReenter and nr.sample() < self.reenter_prob:
            self.reenter += 1
            self.add_to_queue()

        return 1



    def event_based_modelling(self, a, b, m, d):
        req_generator =  UniformGenerator(a, b) 
        req_proccessor = NormalGenerator(m, d)

        req_done_count = 0
        t_generation = req_generator.generate()
        t_proccessor = t_generation + req_proccessor.generate()

        while req_done_count < self.req_count:
            if t_generation <= t_proccessor:
                self.add_to_queue()
                t_generation += req_generator.generate()
                continue
            if t_generation >= t_proccessor:
                req_done_count += self.rem_from_queue(True)
                t_proccessor += req_proccessor.generate()
            
        return (self.queue_len_max, self.req_count, self.reenter)
            


    def time_based_modelling(self, a, b, m, d):

        req_generator =  UniformGenerator(a, b) 
        req_proccessor = NormalGenerator(m, d)

        req_done_count = 0
        t_generation = req_generator.generate()
        t_proccessor = t_generation + req_proccessor.generate()

        t_curr = 0
        while req_done_count < self.req_count:
            if t_generation <= t_curr:
                self.add_to_queue()
                t_generation += req_generator.generate()
            if t_curr >= t_proccessor:
                if self.queue > 0:
                    req_done_count += self.rem_from_queue(True)
                    t_proccessor += req_proccessor.generate()
                else:
                    t_proccessor = t_generation + req_proccessor.generate()

            t_curr += self.dt
        
        return (self.queue_len_max, self.req_count, self.reenter)



