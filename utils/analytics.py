def get_kpis(df):

    total_sessions = len(df)

    unique_users = df[
        "mac_address_hashed"
    ].nunique()

    total_data = (
        df["data_mb"].sum()
    )

    avg_duration = (
        df["connection_duration_secs"]
        .mean()/60
    )

    active_hotspots = (
        df["node_id"].nunique()
    )

    return {
        "sessions": total_sessions,
        "users": unique_users,
        "data": total_data,
        "duration": avg_duration,
        "hotspots": active_hotspots
    }
