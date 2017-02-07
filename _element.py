from selenium.webdriver.common.by import By

class _loginElement(object):
    ''' '''
    username_inputText=(By.ID,'username')
    password_inputText=(By.ID,'password')
    submit_inputText=(By.ID,'login_submit')

class _createUserElement(object):
    '''

    '''
    search_inputText = (By.ID, 'q_simpleSearch')
    search_button = (By.ID, 'btnSimpleSearch')
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
    edit_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[9]/a')
    user_checkbox=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[1]/input')
    groupedit_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[7]/a')

class _linkDepElement(object):
    '''

    '''
    link_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[8]/td[8]/a[2]/i')
    edit_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[10]/td[8]/a[1]/i')
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
    roles_checkbox=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[10]/td[1]/input')
    reason_textarea=(By.XPATH,'//div[@class="modal-body"]/button[@style="float:left"]/textarea')
    group_checkbox=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[1]/input')
    rank_editbutton=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[8]/a[1]')
    rank_checkbox=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[1]/input')
    position_editbutton=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[1]/td[8]/a')
    position_delebutton=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr/td[8]/a[3]/i')

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
    edit_button=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[6]/a')
    org_checkbox=(By.XPATH,'html/body/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[1]/input')

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
    complte_button=(By.ID,'btnCom')
    delete_button=(By.ID,'btnDel')
    content_textarea=(By.ID,'entity_taskContent')

class _createTemplate(object):
    '''

    '''
    templateCode_inputText=(By.ID,'entity_tplCode')
    templateName_inputText=(By.ID,'entity_tplName')
    textField_redioText=(By.ID,'entity_tplType0')
    content_textarea=(By.ID,'entity_tplContent0')
    textEditor_redioText=(By.ID,'entity_tplType1')
    editor_viewText=(By.XPATH,'/html/body')
