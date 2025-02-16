'''
July 2023 by Bruno Batinica
Modelled on code written by Sebastiano Barbieri
s.barbieri@unsw.edu.au
https://www.github.com/sebbarb/
'''

import torch
import optuna
from datetime import datetime
from pdb import set_trace as bp

class Hyperparameters:
    def __init__(self, trial=None):
    
        ### General #########################################################
        
        self.gender = 'males'
        self.min_count = 500 # codes whose occurrence is less than min_count are encoded as OTHER
        self.num_folds = 5
        self.num_trials = 10
        
        # Data
        self.data_dir = 'C:/Users/bruno/OneDrive - The University of Auckland/Documents/Code/python/deep_learning/elective_test/'
        self.data_pp_dir = 'C:/Users/bruno/OneDrive - The University of Auckland/Documents/Code/python/deep_learning/elective_test/pp_data/'
        self.log_dir = self.data_dir + 'log_' + self.gender + '/'
        self.results_dir = self.data_dir + 'results/'
        self.plots_dir = self.results_dir + 'plots/'
        
        # Seeds
        self.np_seed = 1234
        self.torch_seed = 42
        
        # Training
        if torch.cuda.is_available():
            self.device = torch.device('cuda:0')
            torch.backends.cudnn.benchmark = True
        else:
            self.device = torch.device('cpu')


        ### Model ###########################################################
        #### HAVE NOT CHECKED THROUGH YET ######################

        self.batch_size = 256
        self.max_epochs = 10
        self.patience = 10 # early stopping
        self.num_months_hx = 60
        now = datetime.now() # current date and time
        self.model_name = now.strftime('%Y%m%d_%H%M%S_%f') + '.pt'
            
        # Network
        if trial:
            self.nonprop_hazards = trial.suggest_categorical('nonprop_hazards', [True, False])
            self.embedding_dim = trial.suggest_categorical('embedding_dim', [16, 32, 64, 128])
            self.rnn_type = trial.suggest_categorical('rnn_type', ['GRU', 'LSTM'])
            self.num_rnn_layers = trial.suggest_int('num_rnn_layers', 1, 3)
            if self.num_rnn_layers > 1:
                self.dropout = trial.suggest_discrete_uniform('dropout', 0.0, 0.5, 0.1)
            else:
                self.dropout = trial.suggest_discrete_uniform('dropout', 0.0, 0.0, 0.1)
            self.num_mlp_layers = trial.suggest_int('num_mlp_layers', 0, 2)
            self.add_diagt = trial.suggest_categorical('add_diagt', [True, False])
            self.add_month = trial.suggest_categorical('add_month', ['ignore', 'concat', 'embedding'])
            self.summarize = trial.suggest_categorical('summarize', ['hidden', 'output_max', 'output_sum', 'output_avg', 'output_attention'])
            self.learning_rate = trial.suggest_categorical('learning_rate', [1e-4, 1e-3, 1e-2])
        else:
            self.nonprop_hazards = False
            self.embedding_dim = 32
            self.rnn_type = 'GRU'
            self.num_rnn_layers = 3
            self.dropout = 0.1
            self.num_mlp_layers = 1
            self.add_diagt = True
            self.add_month = 'concat'
            self.summarize = 'output_attention'
            self.learning_rate = 1e-3
        
        self.redundant_predictors = True
        self.reduced_col_list = ['nhi_age', 'en_nzdep_q', 'en_prtsd_eth_2', 'en_prtsd_eth_3', 'en_prtsd_eth_9', 'en_prtsd_eth_43']



