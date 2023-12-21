import {createRouter, createWebHistory} from 'vue-router'
import AboutView from "../views/AboutView.vue";
import CatalogView from "../views/CatalogView.vue";
import ContactsView from "../views/ContactsView.vue";
import DeliveryView from "../views/DeliveryView.vue";
import MainView from "../views/MainView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import OrderView from "../views/OrderView.vue";
import PolicyView from "../views/PolicyView.vue";
import ProductView from "../views/ProductView.vue";
import ReviewView from "../views/ReviewView.vue";


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/about',
            name: 'about',
            component: AboutView
        },
        {
            path: '/catalog',
            name: 'catalog',
            component: CatalogView
        },
        {
            path: '/contacts',
            name: 'contacts',
            component: ContactsView
        },
        {
            path: '/delivery',
            name: 'delivery',
            component: DeliveryView
        },
        {
            path: '/',
            name: 'main',
            component: MainView
        },
        {
            path: '/cart',
            name: 'cart',
            component: OrderView
        },
        {
            path: '/policy',
            name: 'policy',
            component: PolicyView
        },
        {
            path: '/catalog/:id',
            name: 'product',
            component: ProductView
        },
        {
            path: '/reviews',
            name: 'reviews',
            component: ReviewView
        },
        {
            path: '/:catchAll(.*)',
            name: 'not-found',
            beforeEnter: (to, from, next) => {
                to.fullPath = decodeURIComponent(to.fullPath);
                next();
            },
            component: NotFoundView
        },
    ]
})

export default router
