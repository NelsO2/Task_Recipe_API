from rest_framework import serializers
from main.models import Recipe, Tag, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """serializer for Ingredients"""

    class Meta:
        model = Ingredient
        fieds = ['id', 'name']
        read_only_fields = ['id']

class TagSerializer(serializers.ModelSerializer):
    """serializer for Tag"""

    class Meta:
        model = Tag
        fieds = ['id', 'name']
        read_only_fields = ['id']


class RecipeSerializer(serializers.ModelSerializer):
    """serializer for recipes"""
    tags = TagSerializer(many=True, required=-False)
    """Nested serializer"""
    Ingredients = IngredientSerializer(many=True, required=-False)


    class Meta:
        model = Recipe
        fields = ['id', 'title', 'tag', 'link', 'tags', 'ingredients']
        read_only_fields = ['id']

    def _get_or_create_tags(self, tags, recipe):
         """refactoring the code"""
         auth_user = self.context['request'].user
         for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(user=auth_user, **tag)
            recipe.tags.add(tag_obj)

    def _get_or_create_ingredients(self, ingredients, recipe):
        """handle getting or creating ingredients as needed"""
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create(user=auth_user, **ingredient)
            recipe.ingredients.add(ingredient_obj)

    def create(self, validated_data):
        """custom logic to create recipe"""
        tags = validated_data.pop('tags', [])
        ingredients = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        self._get_or_create_ingredients(ingredients, recipe)

        return recipe

    def update(self, instance, validated_data):
        """update recipe"""
        tags = validated_data.pop('tags', None)
        ingredients = validated_data.pop('ingredients', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)

        if ingredients is not None:
            instance.ingredients.clear()
            self._get_or_create_ingredients(ingredients, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

            instance.save()
            return instance


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view"""

    class Meta(RecipeSerializer.Meta):
        """using the meta class inside the recipe serializer and passsing
        in the method class, to get all of the mta values that were provided """
        fields = RecipeSerializer.Meta.fields + ['description']
