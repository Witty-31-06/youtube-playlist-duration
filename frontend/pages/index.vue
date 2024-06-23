<script setup lang="ts">
const colorMode = useColorMode()
const isDark = computed({
  get () {
    return colorMode.value === 'dark'
  },
  set () {
    colorMode.preference = colorMode.value === 'dark' ? 'light' : 'dark'
  }
})

const q = ref('')
function lol() {
  console.log("haha")
}
</script>


<template>
  <ClientOnly>
    <UButton
      :icon="isDark ? 'i-heroicons-moon-20-solid' : 'i-heroicons-sun-20-solid'"
      color="gray"
      variant="ghost"
      aria-label="Theme"
      @click="isDark = !isDark"
    />
    <template #fallback>
      <div class="w-8 h-8" />
    </template>
    <div class="flex justify-center items-center h-full w-full">
      <div class="w-2/4">
        <UInput
          v-model="q"
          name="q"
          placeholder="Search..."
          icon="i-heroicons-magnifying-glass-20-solid"
          autocomplete="off"
          :ui="{ icon: { trailing: { pointer: '' } } }"
          @keyup.enter="lol"
        >
          <template #trailing>
            <UButton
              color="gray"
              variant="link"
              icon="i-heroicons-x-mark-20-solid"
              :padded="false"
              @click="q = ''"
            />
          </template>
        </UInput>
      </div>
      
    </div>
    <div class = "flex justify-center items-center h-full w-full">{{ q }}</div>
  </ClientOnly>
</template>
