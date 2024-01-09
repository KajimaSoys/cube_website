import {createRouter, createWebHistory} from 'vue-router'
import AboutView from "../views/AboutView.vue";
import CatalogView from "../views/CatalogView.vue";
import ContactsView from "../views/ContactsView.vue";
import DeliveryView from "../views/DeliveryView.vue";
import MainView from "../views/MainView.vue";
import NotFoundView from "../views/NotFoundView.vue";
import OrderView from "../views/OrderView.vue";
import PolicyView from "../views/PolicyView.vue";
import TermsView from "../views/TermsView.vue";
import ProductView from "../views/ProductView.vue";
import ReviewView from "../views/ReviewView.vue";


const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/about',
            name: 'about',
            component: AboutView,
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'О магазине'}
                ]
            }
        },
        {
            path: '/catalog',
            name: 'catalog',
            component: CatalogView,
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'Каталог'}
                ]
            }
        },
        {
            path: '/catalog/:categorySlug',
            name: 'catalog-category',
            component: CatalogView,
            // beforeEnter: (to, from, next) => {
            //     next();
            //   },
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'Каталог', link: '/catalog'},
                    {name: 'Категория'}
                ]
            }
        },
        {
            path: '/contacts',
            name: 'contacts',
            component: ContactsView,
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'Контакты'}
                ]
            }
        },
        {
            path: '/delivery',
            name: 'delivery',
            component: DeliveryView,
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'Доставка и оплата'}
                ]
            }
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
            component: PolicyView,
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'Политика конфиденциальности'}
                ]
            }
        },
        {
            path: '/terms',
            name: 'terms',
            component: TermsView,
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'Договор оферты'}
                ]
            }
        },
        {
            path: '/catalog/:categorySlug/:productId',
            name: 'product',
            component: ProductView,
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'Каталог', link: '/catalog'},
                    {name: 'Категория', link: '/catalog/:categorySlug'},
                    {name: 'Товар'}
                ]
            }
        },
        {
            path: '/reviews',
            name: 'reviews',
            component: ReviewView,
            meta: {
                breadcrumb: [
                    {name: 'Главная', link: '/'},
                    {name: 'Отзывы'}
                ]
            }
        },
        {
            path: '/:catchAll(.*)',
            name: 'not-found',
            beforeEnter: (to, from, next) => {
                to.fullPath = decodeURIComponent(to.fullPath);
                next();
            },
            component: NotFoundView,
        },
    ]
})

export default router
