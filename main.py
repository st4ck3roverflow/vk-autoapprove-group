# vk-autoaccept for group - arturyud.in - st4ck3r - aug 2021
import time
import vk_api

import config
import logger


def main():
    # initializing vk api
    vk_session = vk_api.VkApi(login=config.vk_credentials[0], password=config.vk_credentials[1],
                              token=config.vk_credentials[2], config_filename='vk_session.json')
    vk_session.auth()
    vk = vk_session.get_api()
    user_info = vk.account.getProfileInfo()
    logger.log_info(f"Account info: Name: {user_info['first_name']} {user_info['last_name']} ID: {user_info['id']}")
    while True:
        requests_list = vk.groups.getRequests(group_id=config.vk_group_id,
                                              fields="first_name,last_name")  # getting requests
        for i in requests_list["items"]:  # checking every request
            user_name, user_id = i['first_name'] + " " + i['last_name'], i['id']
            vk.groups.approveRequest(group_id=config.vk_group_id, user_id=user_id)  # approving request
            logger.log_info(f"Approved request: Name: {user_name} ID: {user_id}")

        time.sleep(1)  # sleeping for a second to not angry vk


if __name__ == "__main__":
    logger.log_info("VK autoaccept - arturyud.in - 2021")
    try:
        main()
    except Exception as e:
        logger.log_error("Error occurred: " + str(e))
