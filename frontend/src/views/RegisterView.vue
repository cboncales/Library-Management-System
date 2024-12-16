<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const first_name = ref('')
const last_name = ref('')
const email = ref('')
const password = ref('')
const role = ref('Student') // Default role
const errorMessage = ref('')

// Handle registration form submission
const handleRegister = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/register/', {
      first_name: first_name.value,
      last_name: last_name.value,
      email: email.value,
      password: password.value,
      role: role.value,
    })
    alert('Registration successful. Please log in.')
    router.push('/login') // Navigate to the login page after registration
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Failed to register. Please try again.'
  }
}
</script>

<template>
  <v-container class="d-flex flex-column align-center justify-center" style="height: 100vh">
    <v-card class="pa-6" width="400">
      <v-card-title class="text-center">Register</v-card-title>
      <v-card-text>
        <v-text-field label="First Name" v-model="first_name" required></v-text-field>
        <v-text-field label="Last Name" v-model="last_name" required></v-text-field>
        <v-text-field label="Email" v-model="email" type="email" required />
        <v-text-field label="Password" v-model="password" type="password" required />
        <v-select label="Role" v-model="role" :items="['Admin', 'Librarian', 'Student']" required />
        <v-alert v-if="errorMessage" type="error" class="mt-4">
          {{ errorMessage }}
        </v-alert>
      </v-card-text>
      <v-card-actions>
        <v-btn color="primary" block @click="handleRegister">Register</v-btn>
      </v-card-actions>
      <v-divider class="my-4" />
      <p class="text-center">
        Already have an account? <router-link to="/login">Login</router-link>
      </p>
    </v-card>
  </v-container>
</template>
