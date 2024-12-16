<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const email = ref('')
const password = ref('')
const errorMessage = ref('')

// Handle login form submission
const handleLogin = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/login/', {
      email: email.value,
      password: password.value,
    })
    // Assuming the API returns a token
    const { token } = response.data
    localStorage.setItem('token', token)
    router.push('/books') // Navigate to the books page after login
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Failed to log in. Please try again.'
  }
}
</script>

<template>
  <v-container class="d-flex flex-column align-center justify-center" style="height: 100vh">
    <v-card class="pa-6" width="400">
      <v-card-title class="text-center">Login</v-card-title>
      <v-card-text>
        <v-text-field label="Email" v-model="email" type="email" required />
        <v-text-field label="Password" v-model="password" type="password" required />
        <v-alert v-if="errorMessage" type="error" class="mt-4">
          {{ errorMessage }}
        </v-alert>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" block @click="handleLogin">Login</v-btn>
      </v-card-actions>
      <v-divider class="my-4" />
      <p class="text-center">
        Don't have an account? <router-link to="/register">Register</router-link>
      </p>
    </v-card>
  </v-container>
</template>
