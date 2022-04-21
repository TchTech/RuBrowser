import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity

tokenizer = AutoTokenizer.from_pretrained("sberbank-ai/sbert_large_nlu_ru", model_max_length=512)
rubert_model = AutoModel.from_pretrained("rusbert_large")
#rubert_model.cuda()  // IF GPU

def embed_bert_cls(text, model, tokenizer):
    t = tokenizer(text, padding=True, truncation=True, return_tensors='pt')

    with torch.no_grad():
        model_output = model(**{k: v.to(model.device) for k, v in t.items()})

    embeddings = model_output.last_hidden_state[:, 0, :]

    embeddings = torch.nn.functional.normalize(embeddings)

    return embeddings[0].cpu().numpy()

def similarity(query_embed, text):

    text_embed = embed_bert_cls(text, rubert_model, tokenizer)

    return cosine_similarity([text_embed], [query_embed])

def bert_score(query, text):
    query_embed = embed_bert_cls(query, rubert_model, tokenizer)

    score = similarity(query_embed, text)

    return score[0][0]