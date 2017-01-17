from selenium.webdriver.common.by import By

class _loginElement(object):
    ''' '''
    username_inputText=(By.ID,'username')
    password_inputText=(By.ID,'password')
    submit_inputText=(By.ID,'login_submit')

class  _menuElement(object):
    '''

    '''
    user_menuText=(By.ID,'5c831ee5-cb54-4119-8181-f72ca60ee8b7')
    dep_menuText=(By.ID,'15af6e07-33c1-48b2-8cc2-b52be0482d99')
    workflow_menuText=(By.ID,'1d70f44f-1147-445c-81f1-0390f7c4039b')
    organ_menuText=(By.ID,'609831c5-db04-4700-a614-7dab30d9a7c4')
    system_menuText=(By.ID,'6b727058-bf0e-4250-b2e5-cfca6eb40400')

class _submenuElemnet(object):
    '''

    '''
    role_menuText=(By.ID,'83ab8f47-99b0-4277-9ebe-d6303e4f9d5d')
    group_menuText=(By.ID,'41cd4770-eaf9-4130-98b6-3d517f80eda6')
    rank_menuText=(By.ID,'fc235670-7ed1-48f6-be64-1346785627e2')
    position_menuText=(By.ID,'08bfb1d7-9fba-4f58-8b1a-924024e27f46')
    process_menuText=(By.ID,'6d000443-93c7-424f-b5ea-3aa6d48c0b16')
    todo_menuText=(By.ID,'d52c250e-2dc0-4cec-898e-8aba1ead795d')
    complete_menuText=(By.ID,'955317c5-9cfc-44ea-b9b6-c8be337bc1d3')
    manage_menuText=(By.ID,'ea30ab19-9b17-4a09-920f-894c7e4bcf18')
    rule_menuText=(By.ID,'6fad93f5-76d1-422b-bb98-a40d51d9cfb4')
    entrust_menuText=(By.ID,'2585fc36-fd1b-4dde-b91e-d3b8201a967e')
    cc_menuText=(By.ID,'22fd0f3a-3417-4b5a-89b3-4e41f5c56a60')
    calendar_menuText=(By.ID,'0b6c269d-45c8-4142-8d5e-92758de2f7ce')
    task_menuText=(By.ID,'01c567e1-ba29-4386-bf4d-7e7940703acb')


class _createUserElement(object):
    '''

    '''
    search_inputText = (By.ID, 'q_simpleSearch')
    search_button = (By.CLASS_NAME, 'btnSimpleSearch')
    new_button=(By.ID,'btnAddNew')
    dele_checkButton=(By.ID, 'btnDel')
    enabled_button=(By.ID,'btnEnable')
    disabled_button=(By.ID,'btnDisable')
    move_button=(By.ID,'btnMove')
    sort_button=(By.ID,'btnSort')
    copy_button=(By.ID,'btnCopy')
    resetPassword_button=(By.ID,'btnResetPassword')
    resource_button=(By.ID,'btnResource')
    logEvent_button=(By.ID,'logEvent')
    fullname_inputText=(By.ID,'entity_fullName')
    loginname_inputText=(By.ID,'entity_loginName')
    email_inputText=(By.ID,'entity_email')
    mobile_inputText=(By.ID,'entity_mobile')
    id_inputText=(By.ID,'entity_identityCard')
    save_button=(By.ID,'btnSave')
    snew_button=(By.ID,'btnCopySave')
    export_button=(By.ID,'btnExport')
class _linkDepElement(object):
    '''

    '''
    link_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[8]/td[8]/a[2]/i')
    edit_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[8]/td[8]/a[1]/i')
    search_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[8]/td[8]/a[3]/i')
    top_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tfoot/tr/td/div[1]/ul/li[1]/a')
    froward_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tfoot/tr/td/div[1]/ul/li[2]/a')
    back_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tfoot/tr/td/div[1]/ul/li[3]/a')
    end_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tfoot/tr/td/div[1]/ul/li[4]/a')
    page_inputText=(By.XPATH,'//*[@id="gridview"]/tfoot/tr/td/div[2]/div/input')
    go_button=(By.XPATH,'//*[@id="gridview"]/tfoot/tr/td/div[2]/div/button')
    check_button=(By.XPATH,'html/body/div[1]/div[1]/div[1]/table/tbody/tr[3]/td[1]/input')
    submit_button=(By.XPATH,'//div[@class="modal-footer"]/button[@class="btn btn-primary save ax-save"]')
    link_to_org_button=(By.ID,'btnlikeOrganization')
    link_to_role_button=(By.ID,'btnlikeRoles')

class _logoutElement(object):
    '''

    '''
    admin_button=(By.ID,'abc')
    logout_button=(By.CLASS_NAME,'icon-off')
    yes_button=(By.XPATH,'//div[@class="modal-footer"]/button[@class="btn btn-primary save ax-save"]')
class _createDep(object):
    '''
    '''
    rolename_inputText=(By.ID,'entity_roleName')
    groupname_inputText=(By.ID,'entity_groupName')
    rankname_inputText=(By.ID,'entity_rankName')
    positionname_inputText=(By.ID,'entity_positionName')

class _createWork(object):
    '''
    '''
    processname_inputText=(By.ID,'entity_name')
    processkey_inputText=(By.ID,'entity_key')

class _craeteOrg(object):
    '''

    '''
    orgname_inputText=(By.ID,'entity_organizationName')
    office_inputText=(By.ID,'entity_officeNo')
    emmail_inputText=(By.ID,'entity_email')

class _createCal(object):
    '''

    '''
    year_buutonText=(By.XPATH,'//div[@class="btn-group"]/button[@class="btn btn-warning btn-primary active"]')
    month_buttonText=(By.XPATH,'//div[@class="btn-group"]/button[@data-calendar-view="month"]')
    week_buttonText=(By.XPATH,'//div[@class="btn-group"]/button[@data-calendar-view="week"]')
    day_buttonText=(By.XPATH,'//div[@class="btn-group"]/button[@data-calendar-view="day"]')
    prev_buttonText=(By.XPATH,'//div[@class="btn-group"]/button[@data-calendar-nav="prev"]')
    today_buttonText=(By.XPATH,'//div[@class="btn-group"]/button[@data-calendar-nav="today"]')
    next_buttonText=(By.XPATH,'//div[@class="btn-group"]/button[@data-calendar-nav="next"]')
    new_buttonText=(By.ID,'btnAddNew')
    reminderContent_inputText=(By.ID,'entity_calSubject')
    starttime_inputText=(By.XPATH,'//*[@id="eidtForm"]/div[3]/div[2]/div/span')
    iframe=(By.XPATH,'//div/iframe')
    day_checkbutton=(By.XPATH,'//tr/td[@onclick="day_Click(2017,1,16);"]')
    endtime_inputText=(By.ID,'entity_endTime')
    type_select=(By.NAME,'calType')
    reminder_select=(By.ID,'tiggerPreTime')
    repeat_select=(By.ID,'tiggerFrequency')
    location_inputText=(By.ID,'entity_calLocation')
    im_checkbox=(By.ID,'entity_notice0')
    system_checkbox=(By.ID,'entity_notice1')
    sms_checkbox=(By.ID,'entity_notice2')
    email_checkbox=(By.ID,'entity_notice3')
    save_button=(By.XPATH,'//div[@class="modal-footer"]/button[@class="btn btn-primary save ax-save"]')
    close_button=(By.XPATH,'//div[@class=""]/button[@class="btn ax-close"]')

class _createTask(object):
    '''

    '''
    new_button=(By.ID,'btnAddNew')