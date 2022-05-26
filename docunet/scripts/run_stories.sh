#! /bin/bash
#export CUDA_VISIBLE_DEVICES=0

# -------------------Training Shell Script--------------------
if true; then
  transformer_type=bert
  channel_type=context-based
  if [[ $transformer_type == bert ]]; then
    bs=4
    bl=3e-5
    uls=(3e-4)
    accum=1
    for ul in ${uls[@]}
    do
    python -u ./train_balanceloss.py --data_dir ./dataset/stories \
    --channel_type $channel_type \
    --bert_lr $bl \
    --transformer_type $transformer_type \
    --model_name_or_path bert-base-cased \
    --train_file train.json \
    --dev_file dev.json \
    --test_file test.json \
    --train_batch_size $bs \
    --test_batch_size $bs \
    --gradient_accumulation_steps $accum \
    --num_labels 1 \
    --learning_rate $ul \
    --max_grad_norm 1.0 \
    --warmup_ratio 0.06 \
    --evaluation_steps 100 \
    --num_train_epochs 2505 \
    --seed 66 \
    --num_class 13 \
    --save_path ./checkpoint/stories/train_bert-lr${bl}_accum${accum}_unet-lr${ul}_type_${channel_type}.pt \
    --log_dir ./logs/stories/train_bert-lr${bl}_accum${accum}_unet-lr${ul}_type_${channel_type}.log
    done
  elif [[ $transformer_type == roberta ]]; then
    type=context-based
    bs=2
    bls=(3e-5)
    ul=4e-4
    accum=2
    for bl in ${bls[@]}
    do
    python -u ./train_balanceloss.py --data_dir ./dataset/stories \
    --channel_type $channel_type \
    --bert_lr $bl \
    --transformer_type $transformer_type \
    --model_name_or_path roberta-large \
    --train_file train.json \
    --dev_file dev.json \
    --test_file test.json \
    --train_batch_size $bs \
    --test_batch_size $bs \
    --gradient_accumulation_steps $accum \
    --num_labels 2 \
    --learning_rate $ul \
    --max_grad_norm 1.0 \
    --warmup_ratio 0.06 \
    --evaluation_steps 100 \
    --num_train_epochs 2505 \
    --seed 111 \
    --num_class 13 \
    --save_path ./checkpoint/stories/train_roberta-lr${bl}_accum${accum}_unet-lr${ul}_type_${channel_type}.pt \
    --log_dir ./logs/stories/train_roberta-lr${bl}_accum${accum}_unet-lr${ul}_type_${channel_type}.log
    done
  fi
fi
