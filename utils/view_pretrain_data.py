from datasets import load_dataset

pretrain_data_meta = load_dataset("liuhaotian/LLaVA-Pretrain", data_files={'train':'blip_laion_cc_sbu_558k_meta.json'})
pretrain_data = load_dataset("liuhaotian/LLaVA-Pretrain", data_files={'train':'blip_laion_cc_sbu_558k.json'})

print(pretrain_data['train'][1])
print(pretrain_data_meta['train'][1])

finetuning_data = load_dataset("liuhaotian/LLaVA-Instruct-150K", data_files= {'train':'llava_instruct_150k.json'})
print(finetuning_data['train'][1])