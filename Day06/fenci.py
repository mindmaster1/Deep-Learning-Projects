import jieba

words1 = "婕婕公主超级美"

words2 = jieba.cut(words1)

print("/".join(words2))