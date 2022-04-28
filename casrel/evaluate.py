#! -*- coding:utf-8 -*-
from data_loader import data_generator, load_data
from model import E2EModel, Evaluate
from utils import extract_items, get_tokenizer, eval_model
import os, argparse
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
from keras import backend as K
if(K.backend() == 'tensorflow'):
    import tensorflow as tf
    from keras.backend.tensorflow_backend import set_session
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    sess = tf.Session(config=config)

parser = argparse.ArgumentParser(description='Model Controller')
parser.add_argument('--dataset', default='WebNLG', type=str, help='specify the dataset from ["NYT","WebNLG","ACE04","NYT10-HRL","NYT11-HRL","Wiki-KBP"]')
args = parser.parse_args()


if __name__ == '__main__':
    # pre-trained bert model config
    bert_model = 'cased_L-12_H-768_A-12'
    bert_config_path = 'pretrained_bert_models/' + bert_model + '/bert_config.json'
    bert_vocab_path = 'pretrained_bert_models/' + bert_model + '/vocab.txt'
    bert_checkpoint_path = 'pretrained_bert_models/' + bert_model + '/bert_model.ckpt'

    dataset = args.dataset
    eval_path = 'data/stories/input.json' # overall test
    rel_dict_path = 'data/' + dataset + '/rel2id.json'
    save_weights_path = 'saved_weights/' + dataset + '/best_model.weights'
    
    LR = 1e-5
    tokenizer = get_tokenizer(bert_vocab_path)
    train_data, dev_data, eval_data, id2rel, rel2id, num_rels = load_data(eval_path, eval_path, eval_path, rel_dict_path)
    subject_model, object_model, hbt_model = E2EModel(bert_config_path, bert_checkpoint_path, LR, num_rels)
    
    hbt_model.load_weights(save_weights_path)
    eval_result_path = 'results/stories/eval_result.json'
    eval_model(subject_model, object_model, eval_data, id2rel, tokenizer, eval_result_path)

