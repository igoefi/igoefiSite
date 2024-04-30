<template>
    <div class="page-category">
        <div class="column is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
            </div>
            <div class="column is-3" 
                v-for="product in products"
                v-bind:key="product.id">
                <div class="box">
                    <figure class="image mb-4">
                    <img :src="product.get_thrumbnail">
                    </figure>

                    <h3 class="is-size-4">{{ product.name }}</h3>
                    <p class="is-size-6 has-text-grey">${{ product.price }}</p>

                    <RouterLink v-bind:to="product.get_absolute_url" class="button is_dark mt-4">View details</RouterLink>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import {toast} from 'bulma-toast'
export default {
    name: 'Category',
    data(){
        return {
            category: {
                products: []
            }
        }
    },
    mounted(){
        this.getCategory()
    },
    methods: {
        getCategory() {
            const categorySlug = this.$route.params.category_slug

            axios
                .get(`/api/v1/products/${categorySlug}/`)
                .then(response => {
                    this.category = response.data
                    document.title = this.category.name
                })
                .catch(error => {
                    console.log(error)

                    toast({
                        message: 'Something wrong. Try again',
                        type: 'is-danger',
                        pauseOnHover:true,
                        duration: 2000,
                        position: 'bottom-left'
                    })
                })
        }
    }
}
</script>