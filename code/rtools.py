def get_user_plan(user_id, users_pd):
    return users_pd[users_pd.user_id == user_id].iloc[0].to_dict()['plan']
