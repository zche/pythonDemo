export BERT_BASE_DIR=/finetune/chinese_wwm_ext_L-12_H-768_A-12
export MY_DATASET=/finetune/data

python3 /finetune/run_classifier.py \
  --task_name rasajson \
  --do_train \
  --do_eval \
  --data_dir $MY_DATASET \
  --vocab_file $BERT_BASE_DIR/vocab.txt \
  --bert_config_file $BERT_BASE_DIR/bert_config.json \
  --init_checkpoint $BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length 64 \
  --train_batch_size 32 \
  --learning_rate 2.5e-5 \
  --warmup_proportion 0.1 \
  --iterations_per_loop 1000 \
  --num_train_epochs 5.0 \
  --output_dir /finetune/rasa_model_output/
