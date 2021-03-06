# Testing Documentation

## Lighthouse Results

|Page|Device|Result|
|-----|-----|-----|
|Home|Desktop|![result Preview](static/images/readme/lighthouse-results/index-desktop.png)|
|Home|Mobile|![result Preview](static/images/readme/lighthouse-results/index-mobile.png)|
|Returns|Desktop|![result Preview](static/images/readme/lighthouse-results/returns-desktop.png)|
|Returns|Mobile|![result Preview](static/images/readme/lighthouse-results/returns-mobile.png)|
|Contact|Desktop|![result Preview](static/images/readme/lighthouse-results/contact-desktop.png)|
|Contact|Mobile|![result Preview](static/images/readme/lighthouse-results/contact-mobile.png)|
|Vehicles|Desktop|![result Preview](static/images/readme/lighthouse-results/vehicle-desktop.png)|
|Vehicles|Mobile|![result Preview](static/images/readme/lighthouse-results/vehicle-mobile.png)|
|Vehicle Detail|Desktop|![result Preview](static/images/readme/lighthouse-results/vehicle-detail-desktop.png)|
|Vehicle Detail|Mobile|![result Preview](static/images/readme/lighthouse-results/vehicle-detail-mobile.png)|
|Vehicle CHeckout|Desktop|![result Preview](static/images/readme/lighthouse-results/vehile_checkout-desktop.png)|
|Vehicle Checkout|Mobile|![result Preview](static/images/readme/lighthouse-results/vehile_checkout-mobile.png)|
|Accessory Categories|Desktop|![result Preview](static/images/readme/lighthouse-results/accessories-desktop.png)|
|Accessory Categories|Mobile|![result Preview](static/images/readme/lighthouse-results/accessories-mobile.png)|
|Accessories Search|Desktop|![result Preview](static/images/readme/lighthouse-results/accessories-search-desktop.png)|
|Accessories Search|Mobile|![result Preview](static/images/readme/lighthouse-results/accessories-search-mobile.png)|
|Accessory Detail|Desktop|![result Preview](static/images/readme/lighthouse-results/accessot-detail-desktop.png)|
|Accessory Detail|Mobile|![result Preview](static/images/readme/lighthouse-results/accessot-detail-mobile.png)|
|Bag|Desktop|![result Preview](static/images/readme/lighthouse-results/bag-desktop.png)|
|Bag|Mobile|![result Preview](static/images/readme/lighthouse-results/bag-mobile.png)|
|Checkout|Desktop|![result Preview](static/images/readme/lighthouse-results/checkout-desktop.png)|
|Checkout|Mobile|![result Preview](static/images/readme/lighthouse-results/checkout-desktop.png)|
|Checkout Success|Desktop|![result Preview](static/images/readme/lighthouse-results/checkout-success-desktop.png)|
|Checkout Success|Mobile|![result Preview](static/images/readme/lighthouse-results/checkout-success-mobile.png)|
|Login|Desktop|![result Preview](static/images/readme/lighthouse-results/login-desktop.png)|
|Login|Mobile|![result Preview](static/images/readme/lighthouse-results/login-mobile.png)|
|Logout|Desktop|![result Preview](static/images/readme/lighthouse-results/logout-desktop.png)|
|Logout|Mobile|![result Preview](static/images/readme/lighthouse-results/logout-mobile.png)|
|Profile|Desktop|![result Preview](static/images/readme/lighthouse-results/profile-desktop.png)|
|Profile|Mobile|![result Preview](static/images/readme/lighthouse-results/profile-mobile.png)|
|Management Home|Desktop|![result Preview](static/images/readme/lighthouse-results/management-home-desktop.png)|
|Management Home|Mobile|![result Preview](static/images/readme/lighthouse-results/management-home-mobile.png)|
|Add Vehicle|Desktop|![result Preview](static/images/readme/lighthouse-results/add-vehicle-desktop.png)|
|Add Vehicle|Mobile|![result Preview](static/images/readme/lighthouse-results/add-vehicle-mobile.png)|
|Add Accessory|Desktop|![result Preview](static/images/readme/lighthouse-results/add-accessory-desktop.png)|
|Add Accessory|Mobile|![result Preview](static/images/readme/lighthouse-results/add-accessory-desktop.png)|
|Update Vehicle|Desktop|![result Preview](static/images/readme/lighthouse-results/update-vehicle-desktop.png)|
|Update Vehicle|Mobile|![result Preview](static/images/readme/lighthouse-results/update-vehicle-mobile.png)|
|Update Accessory|Desktop|![result Preview](static/images/readme/lighthouse-results/update-accesory-desktop.png)|
|Update Accessory|Mobile|![result Preview](static/images/readme/lighthouse-results/update-accesory-mobile.png)|
|Vehicle Orders|Desktop|![result Preview](static/images/readme/lighthouse-results/manage-vehicle-orders-mobile.png)|
|Vehicle Orders|Mobile|![result Preview](static/images/readme/lighthouse-results/manage-vehicle-orders-mobile.png)|
|Accessory Orders|Desktop|![result Preview](static/images/readme/lighthouse-results/manage-accessory-orders-desktop.png)|
|Accessory Orders|Mobile|![result Preview](static/images/readme/lighthouse-results/manage-accessory-orders-mobile.png)|
|Update Order|Desktop|![result Preview](static/images/readme/lighthouse-results/update-order-desktop.png)|
|Update Order|Mobile|![result Preview](static/images/readme/lighthouse-results/update-order-mobile.png)|

## Testing
### Process

#### User

- Load Site
- Click a link to search for a vehicle or search for make / model of car
- View search results
- Reset search page
- Filter vehicles
- View results
- Click on a vehicle
- Click reserve vehicle
- Enter use details and card details
- Make payment
- View success screen
- Register for an account
- Click on Accessories
- Choose and accessory, add to basket
- Choose another accessory, add multiple to basket
- Click on bag
- Click Secure Checkout
- Enter details and make payment
- View success page
- View profile
- View order

#### Admin

- Click Manage
- Click Add Vehicle
- Fill out info, upload pictures
- Click Add Vehicle
- Click Update
- Change some text and add an image and change main image
- Click Update
- Click Delete
- Click Manage
- Click Add Accessory
- Fill out info and add picture
- Click Add Accessory
- Click Update
- Change text
- Click Update
- Click Delete
- Check vehicle orders, filter for paid
- Click to Update order
- Update status

### Testing in Chrome Developer Tools
### iPhone SE 375x667

- Vehicle reserve button's POST request didn't have an order_type
- JS active on management home, removed
- new accessory add not saving
- Confirmation to delete on accessory page not active
- Order number too long on small screens
---
### iPhone XR 414x896
- No issues found

---
### iPad mini 768x1024

- vehicle reserve page, complete button to the left
- Price not on acessory detail

---
### iPad Air 820x1180]
- No issues found
---
## Handheld Device Realworld Testing - Testing Log
---
### iPhone 13 Pro Max (Safari)

- No issues found
### iPhone 13 Pro Max (Chrome)

- No issues found
---
### iPhone 12 Pro (Safari)

- No issues found
---
### iPad Pro 11" (Safari)

- No Issues found
---
### Samsung A40 (Chrome)

- No Issues found
---
## Screen Testing - Testing Log
---

### Laptop 16" Screen 3072x1920

- When no image present on vehicle, coming soon image not showing
- Remembered mileage not working on vehicle search due to typo

---
### iMac 5k 27" Screen 5120x2880

- No issues found
---