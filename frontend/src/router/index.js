import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Users/DashboardView.vue'
import Books from '@/views/Users/BookView.vue'
import Users from '@/views/Staff/UserView.vue'
import Borrow from '@/views/Users/BorrowView.vue'
import Login from '@/views/LoginView.vue'
import Register from '@/views/RegisterView.vue'

// Function to check if user is authenticated
// const isAuthenticated = () => {
//   return !!localStorage.getItem('token') // Returns true if token exists
// }

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/login', // Redirect root to login
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
    },
    {
      path: '/home',
      name: 'home',
      component: Home,
      // meta: { requiresAuth: true }, // Requires authentication
    },
    {
      path: '/books',
      name: 'books',
      component: Books,
      // meta: { requiresAuth: true }, // Requires authentication
    },
    {
      path: '/users',
      name: 'users',
      component: Users,
      // meta: { requiresAuth: true }, // Requires authentication
    },
    {
      path: '/borrow',
      name: 'borrow',
      component: Borrow,
      // meta: { requiresAuth: true }, // Requires authentication
    },
  ],
})

// // Global route guard
// router.beforeEach((to, from, next) => {
//   if (to.meta.requiresAuth && !isAuthenticated()) {
//     // Redirect to login if not authenticated
//     next({ name: 'login' })
//   } else if ((to.name === 'login' || to.name === 'register') && isAuthenticated()) {
//     // Redirect to home if accessing login/register while authenticated
//     next({ name: 'home' })
//   } else {
//     next() // Allow navigation
//   }
// })

export default router
