from transformers import MBartTokenizer, MBartForConditionalGeneration

def summ_text(text):

    model_name = "IlyaGusev/mbart_ru_sum_gazeta"
    tokenizer = MBartTokenizer.from_pretrained(model_name)

    model = MBartForConditionalGeneration.from_pretrained(model_name)
    # model.to("cuda")
    print('MODEL LOADED')
    model.to("cpu")
    article_text = text

    input_ids = tokenizer(
        [article_text['Text']],
        max_length=1000,
        truncation=True,
        return_tensors="pt",
    )["input_ids"].to("cpu")

    output_ids = model.generate(
        max_length = 500,
        min_length = 40,
        length_penalty = 5,
        input_ids=input_ids,
        no_repeat_ngram_size=4
    )[0]
    summary = tokenizer.decode(output_ids, skip_special_tokens=True)
    print('SUMMARY DONE')
    return summary
