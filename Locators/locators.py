from selenium.webdriver.common.by import By

# NOTE: Due to the nature of front-end development locators may change and need to be updated.

# Class for main page locators
class MainPageLocators(object):

    # TODO: LOCATORS FOR SEARCH #

    # Search Button
    SearchSubmitButton = (By.ID, "nav-search-submit-button")

    # Search Box 
    SearchBox = (By.NAME, "field-keywords")

    # Drop Down Menu for search box
    SearchDropDownMenu = (By.ID, "searchDropdownBox")

    # "Alexa Skills" search box drop down
    SearchAlexaSkills = (By.XPATH, '//*[@id="searchDropdownBox"]/option[2]')

    # "Amazon Devices" search box drop down
    SearchAmazonDevices = (By.XPATH, '//*[@id="searchDropdownBox"]/option[3]')

    # "Amazon Explore" search box drop down
    SearchAmazonExplore = (By.XPATH, '//*[@id="searchDropdownBox"]/option[4]')

    # "Amazon Fresh" search box drop down
    SearchAmazonFresh = (By.XPATH, '//*[@id="searchDropdownBox"]/option[5]')

    # "Amazon Pharmacy" search box drop down
    SearchAmazonPharmacy = (By.XPATH, '//*[@id="searchDropdownBox"]/option[6]')

    # "Amazon Warehouse" search box drop down
    SearchAmazonWarehouse = (By.XPATH, '//*[@id="searchDropdownBox"]/option[7]')


    # TODO: LOCATORS FOR NAVIGATION HEADERS #

    # "amazon" navigation logo
    AmazonNavLogo = (By.ID, "nav-logo-sprites")

    # "Select your address"
    SelectYourAddress = (By.ID, "glow-ingress-block")

    # "Choose your location" header on pop up window
    ChooseYourLocationHeader = (By.ID, "a-popover-header-1")

    # Language settings Flag
    LanguageSettingsFlag = (By.ID, "icp-nav-flyout")

    # "Learn more" link on hover window
    LearnMoreLink = (By.CLASS_NAME, "icp-helplink")

    # "Hello, Sign in"
    HelloSignIn = (By.ID, "nav-link-accountList")

    # "Sign in" button on hover window
    SignInButton = (By.CLASS_NAME, "nav-action-inner")

    # "Start here." locator on hover window
    StartHere = (By.XPATH, '//*[@id="nav-flyout-ya-newCust"]/a')

    # "Orders & Returns"
    ReturnsOrders = (By.ID, "nav-orders")

    # "Cart"
    Cart = (By.ID, "nav-cart")


    # TODO: LOCATORS FOR "All" HAMBURGER BUTTON #

    # "All" hamburger menu
    AllHamburgerMenu = (By.ID, "nav-hamburger-menu")

    # "Hello, Sign in" header hamburger menu
    HamburgerHelloSignIn = (By.ID, "hmenu-customer-profile")

    # "Trending" hamburger menu
    HamburgerTrendingSubHeader = (By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[1]/div')

    # "Best Sellers" hamburger menu
    HamburgerBestSellers = (By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[2]/a')

    # "New Releases" hamburger menu
    HamburgerNewReleases = (By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[3]/a')

    # "Movers & Shakers" hamburger menu
    HamburgerMoversShakers = (By.XPATH, '//*[@id="hmenu-content"]/ul[1]/li[4]/a')

    
    # TODO: LOCATORS FOR NAVIGATION SUBHEADERS #

    # "Amazon Basics"
    AmazonBasics = (By.XPATH, '//*[@id="nav-xshop"]/a[3]')

    # "Customer Service"
    CustomerService = (By.XPATH, '//*[@id="nav-xshop"]/a[5]')

    # "Prime"
    Prime = (By.XPATH, '//*[@id="nav-link-amazonprime"]')

    # "Try Prime" anchor on hover window
    TryPrimeAnchor = (By.CLASS_NAME, "prime-button-try")


    # TODO: LOCATORS FOR CAROUSEL #

    # Right next Arrow
    RightArrow = (By.CLASS_NAME, "a-carousel-goto-nextpage")

    # Left previous Arrow
    LeftArrow = (By.CLASS_NAME, "a-carousel-goto-prevpage")

    #Carousel image Container
    CarouselContainer = (By.XPATH, '//*[@id="gw-desktop-herotator"]/div')


# Class for results page locators
class ResultsPageLocators(object):

    # TODO: LOCATORS FOR NAVIGATION HEADERS #

    # "Help & Customer Service" header
    HelpCustomerServiceHeader = (By.CLASS_NAME, "cs-help-title")

    # "Language Settings" header
    LanguageSettingsHeader = (By.ID, "icp-language-heading")


    # TODO: LOCATORS FOR CREATE ACCOUNT #

    # "Create account" header
    CreateAccountHeader = (By.CLASS_NAME, "a-spacing-small")

    # "Your name" textbox
    CreateNameBox = (By.ID, "ap_customer_name")

    # "Mobile number or email" textbox
    CreateNumEmailBox = (By.ID, "ap_email")

    # "Password" text box
    CreatePwdBox = (By.ID, "ap_password")

    # "Re-enter password" textbox
    CreateRePwdBox = (By.ID, "ap_password_check")

    # "Continue", "Verify email", and "Verify mobile number" button
    CreateSubmitButton = (By.ID, "continue")

    # "Continue" text on button
    CreateContinueText = (By.CLASS_NAME, "default-text")

    # "Verify email" text on button
    CreateEmailText = (By.CLASS_NAME, "email-text")

    # "Verify mobile number" text on button
    CreateNumText = (By.CLASS_NAME, "phone-text")

    # "Passwords must match" alert
    CreatePwdsAlert = (By.XPATH, '//*[@id="auth-password-mismatch-alert"]/div/div')


    # TODO: LOCATORS FOR SIGN-IN #

    # "Sign-In" header
    SignInHeader = (By.CLASS_NAME, "a-spacing-small")

    # "Email or mobile phone number" textbox
    SignInEmailNumBox = (By.ID, "ap_email")

    # "Continue" authentication button
    SignInContinueButton = (By.ID, "continue")

    # "Password" textbox
    SignInPwdBox = (By.ID, "ap_password")

    # "Sign-In" button
    SignInSubmitButton = (By.ID, "signInSubmit")

    # "There was a problem" alert
    SignInThereWasAProblem = (By.CLASS_NAME, "a-alert-heading")


    # TODO: LOCATORS FOR NAVIGATION SUBHEADERS #

    # "Amazon Best Sellers" header
    AmazonBestSellersHeader = (By.ID, "zg_banner_text")

    # "Amazon Hot New Releases" header
    AmazonHotNewReleasesHeader = (By.ID, "zg_banner_text")

    # "Amazon Movers & Shakers" header
    AmazonMoversShakersHeader = (By.ID, "zg_banner_text")

    # "Amazon Basics" header
    AmazonBasicsHeader = (By.CLASS_NAME, "style__breadcrumb__3KWWY")

    # "Welcome to Amazon Customer Service" header
    AmazonCustServiceHeader = (By.XPATH, '//*[@id="hub-gateway-app-unauth"]/div[1]/div/h1')

    # "Prime" logo
    PrimeLogo = (By.CLASS_NAME, "prime-logo")

    # "Try Prime FREE" submit button
    TryPrimeSubmitButton = (By.CLASS_NAME, "prime-signup-button")


    # TODO: LOCATORS FOR CHECKOUT #

    # "Your Amazon Cart is Empty" header
    CartEmptyText = (By.XPATH, '//*[@id="sc-active-cart"]/div/div/div[2]/div[1]')

    # "Shopping Cart" header
    ShoppingCartHeader = (By.XPATH, '//*[@id="sc-active-cart"]/div/div/div')

    # 3rd image in results list
    ResultsItem = (By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div[5]/div/div/div/div/div/div[1]/div/div[2]')

    # "Add to cart" button
    AddToCartButton = (By.ID, "add-to-cart-button")

    # "No Thanks" button
    NoThanksButton = (By.XPATH, '//*[@id="attachSiNoCoverage"]/span/input')

    # "Go to Cart" button
    GoToCartButton = (By.XPATH, '//*[@id="sw-gtc"]/span/a')

    # "Subtotal (X items)" text
    SubtotalXItems = (By.ID, "sc-subtotal-label-activecart")

    # "Proceed to checkout" button
    ProceedToCheckout = (By.NAME, "proceedToRetailCheckout")

    # "Select a shipping address" header
    SelecAddressHeader = (By.CLASS_NAME, "a-spacing-base")

    #
