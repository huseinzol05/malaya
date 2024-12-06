WANDB_PROJECT="nanot5-base-malaysian-cased-translation-v6-multipack-post" \
torchrun \
--nproc_per_node 4 \
-m run_t5_multipack_compile \
--model_name_or_path mesolitica/nanot5-base-malaysian-translation-v2 \
--num_train_epochs 2 \
--eval_steps 1000000000 \
--logging_steps 2 \
--save_steps 200 \
--save_total_limit 3 \
--do_train \
--train_file /workspace/malaysian-translation-v2-multipack-2048-post \
--output_dir nanot5-base-malaysian-cased-translation-v5-multipack-post \
--dataloader_num_workers 5 \
--dataloader_prefetch_factor 4 \
--per_device_train_batch_size=6 \
--per_device_eval_batch_size=3 \
--gradient_accumulation_steps=5 \
--max_source_length 2048 \
--max_target_length 2048 \
--learning_rate 2e-5 \
--max_grad_norm 1.0 \
--gradient_checkpointing false \
--weight_decay 0.001 \
--bf16 \
--ddp_find_unused_parameters true \
--model_revision 57cebd22c04e2c3ffe4697a1e9dbfa5839e8750c \
--torch_compile
