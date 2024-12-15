import { createRouter, createWebHistory } from 'vue-router'
import Home from './views/Home.vue'
import Books from './views/Books.vue'
import Users from './views/Users.vue'
import Borrow from './views/Borrow.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/books',
      name: 'books',
      component: Books,
    },
    {
      path: '/users',
      name: 'users',
      component: Users,
    },
    {
      path: '/borrow',
      name: 'borrow',
      component: Borrow,
    },
  ],
})

export default router
