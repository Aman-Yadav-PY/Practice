#based on 2019 developers survey on stackoverflow
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-dark')

reader = pd.read_csv('Survey_results_public.csv')

country_group = reader.groupby('Country')

all_user = country_group['SocialMedia'].apply(lambda x: x.str.contains('YouTube').sum())[60:100]
youtube_user = dict(all_user)

for k, v in youtube_user.items():
	plt.barh(k, v)


plt.xlabel('Countries')
plt.ylabel('Number of Users')

plt.tight_layout()
plt.show()















































# import pandas as pd 

# plt.style.use('seaborn-dark')

# reader = pd.read_csv('Survey_results_public.csv')

# values = dict(reader['Hobbyist'].value_counts())
# k, v = values.items()

# plt.bar(k[0], k[1], label='Yes', color='green', alpha=0.5)
# plt.bar(v[0], v[1], label='No', color='red', alpha=0.5)


# plt.legend()
# plt.tight_layout()

# plt.title('Hobbyist in Coding')
# plt.xlabel('Yes/No')
# plt.ylabel('People')


# plt.show()
